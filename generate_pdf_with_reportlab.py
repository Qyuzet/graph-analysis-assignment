from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
import markdown
import re
import io

def extract_sections(markdown_text):
    """
    Extract sections from markdown text
    """
    # Split by headers
    sections = []
    current_section = {"title": "Introduction", "content": ""}
    
    lines = markdown_text.split('\n')
    for line in lines:
        if line.startswith('# '):
            # Main title
            current_section = {"title": line[2:], "content": ""}
            sections.append(current_section)
        elif line.startswith('## '):
            # Section title
            current_section = {"title": line[3:], "content": ""}
            sections.append(current_section)
        elif line.startswith('### '):
            # Subsection title
            current_section = {"title": line[4:], "content": ""}
            sections.append(current_section)
        else:
            # Content
            current_section["content"] += line + "\n"
    
    return sections

def extract_tables(markdown_text):
    """
    Extract tables from markdown text
    """
    tables = []
    table_pattern = r'\|.*\|\n\|[-:|\s]+\|\n(\|.*\|\n)+'
    
    for table_match in re.finditer(table_pattern, markdown_text, re.MULTILINE):
        table_text = table_match.group(0)
        
        # Parse table
        rows = []
        for line in table_text.strip().split('\n'):
            if '|' in line and not line.strip().startswith('|-'):
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                rows.append(cells)
        
        if rows:
            tables.append(rows)
    
    return tables

def create_pdf(markdown_file, pdf_file):
    """
    Create PDF from markdown file using ReportLab
    """
    # Read markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    # Extract sections and tables
    sections = extract_sections(markdown_text)
    tables = extract_tables(markdown_text)
    
    # Create PDF document
    doc = SimpleDocTemplate(pdf_file, pagesize=letter, 
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=72)
    
    # Define styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Title', 
                             fontName='Helvetica-Bold',
                             fontSize=18, 
                             alignment=1,  # Center
                             spaceAfter=12))
    
    styles.add(ParagraphStyle(name='Heading1', 
                             fontName='Helvetica-Bold',
                             fontSize=16, 
                             spaceAfter=10))
    
    styles.add(ParagraphStyle(name='Heading2', 
                             fontName='Helvetica-Bold',
                             fontSize=14, 
                             spaceAfter=8))
    
    styles.add(ParagraphStyle(name='Normal', 
                             fontName='Helvetica',
                             fontSize=11, 
                             spaceAfter=6))
    
    # Build document content
    content = []
    
    # Add title
    if sections and "MST and Shortest Path Algorithms Analysis" in sections[0]["title"]:
        content.append(Paragraph(sections[0]["title"], styles['Title']))
        content.append(Spacer(1, 0.25*inch))
    
    # Process sections
    for section in sections[1:]:  # Skip title
        # Add section title
        if "Introduction" in section["title"] or "Algorithm Descriptions" in section["title"] or "Implementation Details" in section["title"] or "Graph Datasets" in section["title"] or "Performance Results" in section["title"] or "Analysis" in section["title"] or "Conclusion" in section["title"] or "Future Work" in section["title"] or "Appendix" in section["title"]:
            content.append(Paragraph(section["title"], styles['Heading1']))
        else:
            content.append(Paragraph(section["title"], styles['Heading2']))
        
        # Add section content
        section_content = section["content"].strip()
        if section_content:
            # Process content paragraphs
            paragraphs = section_content.split('\n\n')
            for para in paragraphs:
                if para.strip():
                    # Check if it's a list
                    if para.strip().startswith('- ') or para.strip().startswith('* '):
                        list_items = para.strip().split('\n')
                        for item in list_items:
                            if item.strip():
                                content.append(Paragraph(item.strip(), styles['Normal']))
                    else:
                        content.append(Paragraph(para.strip(), styles['Normal']))
        
        content.append(Spacer(1, 0.1*inch))
    
    # Add tables
    for table_data in tables:
        if table_data:
            # Create ReportLab table
            table = Table(table_data)
            
            # Add table style
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))
            
            content.append(table)
            content.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(content)
    print(f"PDF report generated: {pdf_file}")

def main():
    markdown_file = 'comprehensive_report.md'
    pdf_file = 'graph_algorithms_report.pdf'
    
    print("Generating PDF report...")
    create_pdf(markdown_file, pdf_file)

if __name__ == "__main__":
    main()

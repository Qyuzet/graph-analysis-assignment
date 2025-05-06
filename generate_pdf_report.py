import markdown
import pdfkit
import os
import sys

def markdown_to_html(markdown_file, html_file):
    """
    Convert markdown file to HTML
    """
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code', 'codehilite'])
    
    # Add CSS for better styling
    css = """
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2, h3, h4 {
            color: #333;
            margin-top: 30px;
        }
        h1 {
            text-align: center;
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        h2 {
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        code {
            background-color: #f5f5f5;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: Consolas, monospace;
        }
        pre {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            color: #777;
            font-size: 0.9em;
            border-top: 1px solid #eee;
            padding-top: 20px;
        }
    </style>
    """
    
    # Complete HTML document
    complete_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>MST and Shortest Path Algorithms Analysis</title>
        {css}
    </head>
    <body>
        {html}
        <div class="footer">
            <p>MST and Shortest Path Algorithms Analysis Report</p>
        </div>
    </body>
    </html>
    """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(complete_html)

def html_to_pdf(html_file, pdf_file):
    """
    Convert HTML file to PDF using pdfkit
    """
    try:
        # Try to find wkhtmltopdf in the system path
        config = pdfkit.configuration()
        pdfkit.from_file(html_file, pdf_file, configuration=config)
        print(f"PDF report generated: {pdf_file}")
    except Exception as e:
        print(f"Error generating PDF: {e}")
        print("Please make sure wkhtmltopdf is installed and in your system path.")
        print("You can download it from: https://wkhtmltopdf.org/downloads.html")
        print(f"HTML report generated: {html_file}")

def main():
    markdown_file = 'comprehensive_report.md'
    html_file = 'graph_algorithms_report.html'
    pdf_file = 'graph_algorithms_report.pdf'
    
    print("Converting markdown to HTML...")
    markdown_to_html(markdown_file, html_file)
    
    print("Converting HTML to PDF...")
    html_to_pdf(html_file, pdf_file)

if __name__ == "__main__":
    main()

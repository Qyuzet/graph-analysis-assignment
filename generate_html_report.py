import markdown
import os

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
        @media print {
            @page {
                size: A4;
                margin: 1cm;
            }
            body {
                font-size: 12pt;
            }
            h1 {
                font-size: 18pt;
            }
            h2 {
                font-size: 16pt;
            }
            h3 {
                font-size: 14pt;
            }
            pre, code {
                font-size: 10pt;
            }
            .no-print {
                display: none;
            }
        }
        
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
        .print-button {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .print-button:hover {
            background-color: #45a049;
        }
    </style>
    """
    
    # Add JavaScript for print functionality
    js = """
    <script>
        function printReport() {
            window.print();
        }
    </script>
    """
    
    # Complete HTML document
    complete_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>MST and Shortest Path Algorithms Analysis</title>
        {css}
        {js}
    </head>
    <body>
        <button class="print-button no-print" onclick="printReport()">Save as PDF</button>
        {html}
        <div class="footer">
            <p>MST and Shortest Path Algorithms Analysis Report</p>
        </div>
    </body>
    </html>
    """
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(complete_html)
    
    print(f"HTML report generated: {html_file}")
    print("Open this file in a web browser and click 'Save as PDF' to generate a PDF version.")

def main():
    markdown_file = 'comprehensive_report.md'
    html_file = 'graph_algorithms_report.html'
    
    print("Converting markdown to HTML...")
    markdown_to_html(markdown_file, html_file)

if __name__ == "__main__":
    main()

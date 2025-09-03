import base64
import plotly.io as pio


# ----------------------------
# Generate styled HTML Report
# ----------------------------
def render_html_report(title, summary, bullets, charts_figs):
    """Generate a full HTML report with summary, insights, and interactive charts."""
    rows = summary.get("shape", {}).get("rows", "N/A")
    cols = summary.get("shape", {}).get("columns", "N/A")
    columns = summary.get("columns", [])

    # --- HTML Structure ---
    html = f"""
    <html>
    <head>
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                background: #FDFEFE;
                color: #2C3E50;
            }}
            h1 {{ color: #2E86C1; }}
            h2 {{ color: #117864; margin-top:30px; }}
            h3 {{ color: #1F618D; }}
            .box {{
                background:#F8F9F9;
                padding:10px;
                border-radius:6px;
                margin-bottom:15px;
                border:1px solid #D5DBDB;
            }}
            .insight {{ margin:6px 0; }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>

        <h2>📊 Dataset Summary</h2>
        <div class="box">
            <b>Rows:</b> {rows}<br>
            <b>Columns:</b> {cols}
        </div>

        <h2>📑 Columns</h2>
        <div class="box">{", ".join(columns) if columns else "No column info available"}</div>

        <h2>💡 Insights</h2>
        <div class="box">
    """
    if bullets:
        for b in bullets:
            html += f"<div class='insight'>✅ {b}</div>"
    else:
        html += "<i>No insights generated.</i>"
    html += "</div>"

    # Charts (interactive Plotly)
    html += "<h2>📈 Charts</h2>"
    if charts_figs:
        for name, fig in charts_figs.items():
            html += f"<h3>{name}</h3>"
            html += pio.to_html(fig, full_html=False, include_plotlyjs="cdn")
    else:
        html += "<i>No charts available.</i>"

    # Footer
    html += """
    <hr>
    <p style="color:gray; font-size:12px;">📄 Auto-generated Dataset Report</p>
    </body></html>
    """
    return html


# ----------------------------
# Download link helper
# ----------------------------
def make_download_link_html(html_str, filename="report.html", mime="text/html"):
    """Return base64 encoded download link for HTML file."""
    b64 = base64.b64encode(html_str.encode()).decode()
    return f"data:{mime};base64,{b64}"

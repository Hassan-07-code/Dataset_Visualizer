import pytest
import plotly.graph_objects as go
from modules.visualization import generate_chart

def test_generate_chart_valid_data():
    """Test generating a valid chart with proper data."""
    data = {
        'x': [1, 2, 3, 4],
        'y': [10, 20, 25, 30],
        'chart_type': 'bar'
    }
    chart = generate_chart(data)
    assert isinstance(chart, go.Figure)
    assert chart.data[0].x.tolist() == data['x']
    assert chart.data[0].y.tolist() == data['y']

def test_generate_chart_empty_data():
    """Test chart generation with empty data."""
    data = {
        'x': [],
        'y': [],
        'chart_type': 'line'
    }
    chart = generate_chart(data)
    assert isinstance(chart, go.Figure)
    assert len(chart.data) == 0

def test_generate_chart_invalid_data():
    """Test mismatched data lengths should raise ValueError."""
    data = {
        'x': [1, 2, 3],
        'y': [10, 20],
        'chart_type': 'scatter'
    }
    with pytest.raises(ValueError):
        generate_chart(data)

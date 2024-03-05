import pytest
from unittest.mock import Mock, patch
from django.conf import settings
from pages.wikipedia_service import get_wikipedia_revisions, generate_graph

def test_generate_graph():
    with patch('pages.wikipedia_service.get_wikipedia_revisions') as mock_get_wikipedia_revisions:
        mock_get_wikipedia_revisions.return_value = [
            {"timestamp": "2022-01-01T00:00:00", "parsedcomment": "Test comment 1"},
            {"timestamp": "2022-01-02T00:00:00", "parsedcomment": "Test comment 2"}
        ]
        result = generate_graph(day=1)
        print(result)
        assert result is not None
        assert isinstance(result, dict)
        assert len(result.keys()) == 3 
        assert len(result['Perovskite_solar_cell'].keys()) == 7
        assert len(result['Solar_cell'].keys()) == 7
        assert len(result['Semiconductor'].keys()) == 7
        assert len(result['Perovskite_solar_cell']['2009-04-14 00:00:00']) == 2
        # assert len(result['Solar_cell']['2009-04-14 00:00:00']) == 2
        # assert len(result['Semiconductor']['2009-04-14 00:00:00']) == 2
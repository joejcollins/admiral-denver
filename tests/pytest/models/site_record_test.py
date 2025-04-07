"""Tests for site_record.py"""

from atlanta_shore.models import site_record

SITE_RECORD_STRING = """quadrat,3,
waypoint,1,
grid_reference,TL6778733146,
photo_up,P2020001,
photo_down,P2020002,
wetness,1,
canopy,5,
species,Urtica dioica,
,Rubus fruticosus agg.,
,Galium aparine,
,Mercurialis perennis,
,Cirsium arvense,
,Juncus effusus,
,Ulmus procera,Changed from U.minor sensu as this species prefers acidic soil and original determination on twigs and dried leaves only.
,Ficaria verna,
,Glechoma hederacea,
,Holcus mollis,
,Brachythecium rutabulum,"""  # noqa: E501


def test_site_record() -> None:
    """Read in a site record and confirm attributes."""
    # ACT
    the_site_record = site_record.SiteRecord(SITE_RECORD_STRING)
    # ASSERT
    assert the_site_record.quadrat["id"] == "3"
    assert the_site_record.waypoint["name"] == "1"

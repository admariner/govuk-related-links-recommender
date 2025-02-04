from src.utils.miscellaneous import read_config_yaml
from src.utils.miscellaneous import parse_sql_script


def test_get_excluded_document_types():
    doc_types = ['about',
                 'about_our_services',
                 'access_and_opening',
                 'business_support_finder',
                 'coming_soon',
                 'complaints_procedure',
                 'completed_transaction',
                 'contact',
                 'corporate_report',
                 'dfid_research_output',
                 'equality_and_diversity',
                 'field_of_operation',
                 'finder',
                 'finder_email_signup',
                 'gone',
                 'help_page',
                 'hmrc_manual_section',
                 'homepage',
                 'html_publication',
                 'licence_finder',
                 'mainstream_browse_page',
                 'manual_section',
                 'media_enquiries',
                 'membership',
                 'ministerial_role',
                 'need',
                 'organisation',
                 'our_energy_use',
                 'our_governance',
                 'person',
                 'personal_information_charter',
                 'placeholder_ministerial_role',
                 'placeholder_person',
                 'placeholder_policy_area',
                 'placeholder_topical_event',
                 'placeholder_world_location_news_page',
                 'policy_area',
                 'publication_scheme',
                 'redirect',
                 'search',
                 'service_manual_guide',
                 'service_manual_homepage',
                 'service_manual_service_standard',
                 'service_manual_service_toolkit',
                 'service_manual_topic',
                 'service_standard_report',
                 'services_and_information',
                 'social_media_use',
                 'special_route',
                 'staff_update',
                 'taxon',
                 'topic',
                 'topical_event',
                 'topical_event_about_page',
                 'travel_advice',
                 'travel_advice_index',
                 'uk_market_conformity_assessment_body',
                 'working_group',
                 'world_location',
                 'worldwide_organisation']

    assert doc_types == read_config_yaml("document_types_excluded_from_the_topic_taxonomy.yml")[
        'document_types']


def test_parse_sql_script():
    query = parse_sql_script('tests/unit/fixtures/test_query.sql')
    assert query == '--Random comment\nSELECT *  from bigtable\n'

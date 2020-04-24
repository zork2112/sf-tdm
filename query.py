#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Stephen Stokes: sstokes[at]relationshipvelocity.com'

import json
import logging

import tools.helpers as h

# Logging setup
h.setup_logging(level=logging.DEBUG)

# Logging statements for each module:
log = logging.getLogger(__name__)
log.debug('Logging is configured.')


# Primary function
@h.timer(log)
def do_query():
    sf_rest = h.get_sf_rest_connection('./config/prs.dev190326.json')

    # query = "select Id, Name, RecordType.Name, ParentId, Parent.Legacy_ID__c, EIN__c from Account"
    # query = "select Id, Name, SobjectType from RecordType where SobjectType = 'Account'"
    # query = "select count(Id) from Account where Legacy_ID__c in ('0013900001PP4E7AAL', '00170000010p2tdAAA')"
    # query = "select Legacy_ID__c, Parent.Legacy_ID__c from Account where Legacy_ID__c in ('0013900001PP4E7AAL', '00170000010p2tdAAA')"
    # query = "select Legacy_ID__c, Parent.Legacy_ID__c from Account where Legacy_ID__c != null"
    # query = "select Name, Type, RecordTypeId, BillingStreet, BillingCity, BillingState, BillingPostalCode, BillingCountry, BillingLatitude, BillingLongitude, BillingGeocodeAccuracy, ShippingStreet, ShippingCity, ShippingState, ShippingPostalCode, ShippingCountry, ShippingLatitude, ShippingLongitude, ShippingGeocodeAccuracy, Phone, Fax, AccountNumber, Website, Sic, Industry, AnnualRevenue, NumberOfEmployees, Ownership, TickerSymbol, Description, Rating, Site, AccountSource, SicDesc, BIS_External_ID__c, Controlled_Grp__c, EIN__c, Fiscal_Year_End__c, Last_Update_User__c, NAICS_Code__c, Client_External_ID__c, DTP_Data_Quality__c, Direct_Contact__c, Acts_as_an_Advisor_Firm__c, Partner_External_ID__c, Custodian_External_ID__c, Trading_Partner_External_ID__c, Advisor_External_ID__c, Last_Update_Date__c, Employer_Division_Restriction__c, Holding_Company__c, Legacy_ID__c, Market_Segment__c, Membership__c, Notes__c, Number_of_Locations__c, Party_Brand__c, Selling_Agreement_Status__c, Vanity_URL__c, Web_Address__c, LID__LinkedIn_Company_Id__c from Account where Legacy_ID__c != null"
    # query = "select Id from Account where Id in (select Id from Account where Legacy_ID__c != null) and ParentId != null"
    # obj = 'WS_Feature_Flag__c'
    # query = f'select count(Id) from {obj}'

    # results = sf_rest.soql_query(query)
    # log.info(f'{obj} - {results}')

    url = "/tooling/executeAnonymous/?anonymousBody=Database.executeBatch(new UuidUtils());"
    results = sf_rest.get_response(url).json()

    with open('./output/query.json', 'w') as json_file:
        json.dump(results, json_file)
    sf_rest.close_connection()

    return len(results)


# Run main program
if __name__ == '__main__':
    log.info(do_query())

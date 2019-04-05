prices=[10,20,30]
total=0
for x in prices:
    total += x

print(f"total : {total} ")
#----------------------------------
# tempdf = df.head()
# tempdf
# nonTextList = ['PT','OT', 'SPEECH THERAPIST', 'PTA', 'RD/LMNT', 'PHYSICAL THERAPIST']
# result = tempdf[~((tempdf['Entity Type Code'] != 1.0) & (tempdf['Provider Credential Text'].isin(nonTextList)))]
# result
# query=N1QLQuery('Select meta().id,dep_flipt_person_id from `'+bucket_name+'`where type="prescriber")
#
# jsondata = {}
# for qres in cb.n1ql_query(query):
# #     if mode.upper().strip()=='FINAL':
#         cb.mutate_in(qres['id'],SD.upsert('ins_carrier',carrier))
#         # cb.mutate_in(qres['id'],SD.upsert('updated_at',current_time))
# else:
#         cb.upsert(str(cb.counter('docid',delta=1).value),jsondata, format=FMT_JSON)

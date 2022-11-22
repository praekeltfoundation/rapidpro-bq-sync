IMPORT_FLOW_DATA = True
HASH_URN = False
CONTACT_FIELDS = {
    "uuid": "STRING",
    "modified_on": "TIMESTAMP",
    "urn": "STRING",
}
ADDITIONAL_CONTACT_PROPERTIES = False  # language, created_on
GROUP_CONTACT_FIELDS = {"group_uuid": "STRING", "contact_uuid": "STRING"}
CONTACT_GROUP_FILTER = None
GROUP_FIELDS = {"name": "STRING", "uuid": "STRING"}
FLOWS_FIELDS = {"labels": "STRING", "name": "STRING", "uuid": "STRING"}
FLOW_RUNS_FIELDS = {
    "modified_on": "TIMESTAMP",
    "responded": "BOOLEAN",
    "contact_uuid": "STRING",
    "flow_uuid": "STRING",
    "exit_type": "STRING",
    "created_on": "TIMESTAMP",
    "exited_on": "TIMESTAMP",
    "id": "INTEGER",
}
FLOW_RUN_VALUES_FIELDS = {
    "input": "STRING",
    "time": "TIMESTAMP",
    "category": "STRING",
    "name": "STRING",
    "value": "STRING",
    "run_id": "INTEGER",
}

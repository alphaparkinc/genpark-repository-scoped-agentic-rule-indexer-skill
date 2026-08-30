from client import RepositoryScopedAgenticRuleIndexerClient

def main():
    client = RepositoryScopedAgenticRuleIndexerClient()
    res = client.index_and_inject_context_rules('/repo/core', 'src/api/auth.ts')
    print('Agentic Rule Indexer: ' + res['rule_index_id'])
    print('Rules Injected: ' + str(len(res['matched_rule_definitions'])) + ' (' + str(res['context_token_overhead']) + ' tokens)')
    for rule in res['matched_rule_definitions']:
        print('  * ' + rule)
    print('Compliance Enforced: ' + str(res['architecture_compliance_enforced']))
    print('Manifest: ' + res['rule_hierarchy_manifest_url'])

if __name__ == '__main__':
    main()

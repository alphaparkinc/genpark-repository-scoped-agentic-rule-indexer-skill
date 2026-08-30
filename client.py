class RepositoryScopedAgenticRuleIndexerClient:
    def index_and_inject_context_rules(self, repo_structure_path='/repo/enterprise-payment', current_active_file='src/domain/billing/invoice.py'):
        return {
            'rule_index_id': 'rul_idx_7721',
            'matched_rule_definitions': [
                'RULE[domain-immutability]: Invoices once persisted cannot be mutated directly',
                'RULE[precision]: Use Decimal with 4 decimal places for all currency amounts'
            ],
            'context_token_overhead': 148,
            'architecture_compliance_enforced': True,
            'rule_hierarchy_manifest_url': 'https://rules.genpark.ai/manifest/7721.json'
        }

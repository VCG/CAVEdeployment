from jinja2 import Environment, FileSystemLoader


def create_double_quoted_list_of_strings(l):
    return ",".join([f'"{s}"' for s in l])


def create_spaced_list_of_strings(l):
    return " ".join([f'"{s}"' for s in l])


var_dict = {
    "environment_name": "depl",
    "project_name": "my_project",
    "pcg_bucket_name": "pcg_bucket",
    "depl_region": "sweet-sweet-kingdom",
    "depl_zone": "sweet-sweet-kingdom-a",
    "dns_zone": "kingdom",
    "domain_name": "domain",
    "letsencrypt_email": "my_email",
    "supported_datastack_list": ["ds1", "ds2"],
    "data_project_name": "data_project",
    "data_project_region": "sweet-sweet-kingdom",
    "docker_repository": "docker.io/caveconnectome",
    "add_dns_hostnames": ["add_hostname1", "add_hostname2"],
    "add_dns_zones": ["$DNS_ZONE", "add_zone"],
    "postgres_password": "my_sweet_secret",
    "sql_instance_name": "daf-depl",
    "bigtable_instance_name": "pychunkedgraph",
    "add_storage_secrets": ["my-secret-secret.json", "my-secret-secret2.json"],
    "mat_health_aligned_volume_name": "volume",
    "mat_datastacks": "datastack1,datastack2",
    "mat_beat_schedule": "environments/local/my_mat_schedule.json",
    "pcg_graph_ids": "pcg_table1,pcg_table2",
    "authservice_secret_key": "randomkey",
    "global_server": "global.my-dns.com",
    "guidebook_csrf_key": "random_key",
    "guidebook_datastack": "datastack0",
    "guideboox_expected_resolution": "4,4,40",
    "dash_secret_key": "random_key",
    "dash_config_filename": "my_dash_config.py",
}

# Additional modifications to parameters and checks
var_dict["supported_datastacks"] = create_double_quoted_list_of_strings(
    var_dict["supported_datastack_list"]
)

var_dict["dns_hostnames"] = create_spaced_list_of_strings(
    ["$DNS_HOSTNAME"] + var_dict["add_dns_hostnames"]
)
var_dict["dns_zones"] = create_spaced_list_of_strings(
    ["$DNS_ZONES"] + var_dict["add_dns_hostnames"]
)
var_dict["pcg_service_account_addon"] = " ".join(
    [
        "".join(["--from-file=", sec, "=${ADD_STORAGE_SECRET_FOLDER}/", sec])
        for sec in var_dict["add_storage_secrets"]
    ]
)


# Load and render template
env = Environment(loader=FileSystemLoader("."))
template = env.get_template("local_env_template.sh")
rendered_template = template.render(var_dict)

# Write rendered tempalte
with open(f"{var_dict['environment_name']}.sh", "w") as f:
    f.write(rendered_template)
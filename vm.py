from datetime import datetime, time
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Azure VM details
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group_name = os.getenv("AZURE_RESOURCE_GROUP")
vm_name = os.getenv("AZURE_VM_NAME")

# Authenticate with Azure using DefaultAzureCredential
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

def start_vm():
    print(f"Starting VM: {vm_name}")
    async_vm_start = compute_client.virtual_machines.begin_start(resource_group_name, vm_name)
    async_vm_start.result()  # Wait for the operation to complete
    print(f"VM {vm_name} started successfully.")

def stop_vm():
    print(f"Stopping VM: {vm_name}")
    async_vm_stop = compute_client.virtual_machines.begin_deallocate(resource_group_name, vm_name)
    async_vm_stop.result()  # Wait for the operation to complete
    print(f"VM {vm_name} stopped successfully.")

def main():
    now = datetime.now().time()

    if time(9, 0) <= now < time(21, 0):
        start_vm()
    else:
        stop_vm()

if __name__ == "__main__":
    main()


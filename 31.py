import pandas as pd  

class HardwareCostEstimator:  
    def __init__(self, iot_device_cost, blockchain_node_cost, integration_device_cost):  
        self.iot_device_cost = iot_device_cost  
        self.blockchain_node_cost = blockchain_node_cost  
        self.integration_device_cost = integration_device_cost  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"File '{file_path}' loaded successfully. Number of rows: {len(df)}")  
        except Exception as e:  
            print(f"Error reading file: {e}")  
            return  

        # Assume 'device_id' column indicates unique IoMT devices; adjust if needed  
        if 'device_id' in df.columns:  
            num_iot_devices = df['device_id'].nunique()  
            print(f"Number of unique IoMT devices: {num_iot_devices}")  
        else:  
            num_iot_devices = 100  # default if column not found  
            print(f"'device_id' column not found. Using default number of IoMT devices: {num_iot_devices}")  

        # Estimate blockchain nodes as one node per 20 IoMT devices (minimum one)  
        num_blockchain_nodes = max(1, num_iot_devices // 20)  

        # Estimate integration devices as 10% of IoMT devices (minimum one)  
        num_integration_devices = max(1, num_iot_devices // 10)  

        # Calculate costs  
        cost_iot_devices = num_iot_devices * self.iot_device_cost  
        cost_blockchain_nodes = num_blockchain_nodes * self.blockchain_node_cost  
        cost_integration_devices = num_integration_devices * self.integration_device_cost  

        total_cost = cost_iot_devices + cost_blockchain_nodes + cost_integration_devices  

        print("\nHardware Cost Summary:")  
        print(f"IoMT Devices ({num_iot_devices} devices): {cost_iot_devices} units")  
        print(f"Blockchain Nodes ({num_blockchain_nodes} nodes): {cost_blockchain_nodes} units")  
        print(f"Integration Devices ({num_integration_devices} devices): {cost_integration_devices} units")  
        print(f"Total Hardware Cost: {total_cost} units\n")  

        return {  
            'num_iot_devices': num_iot_devices,  
            'num_blockchain_nodes': num_blockchain_nodes,  
            'num_integration_devices': num_integration_devices,  
            'cost_iot_devices': cost_iot_devices,  
            'cost_blockchain_nodes': cost_blockchain_nodes,  
            'cost_integration_devices': cost_integration_devices,  
            'total_cost': total_cost  
        }  

if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    #  unit costs (adjust according to your context)  
    iot_device_unit_cost = 500       # Cost per IoMT device  
    blockchain_node_unit_cost = 2000 # Cost per blockchain node  
    integration_device_unit_cost = 300 # Cost per integration device  

    estimator = HardwareCostEstimator(iot_device_unit_cost, blockchain_node_unit_cost, integration_device_unit_cost)  
    cost_summary = estimator.estimate_costs(file_path)  
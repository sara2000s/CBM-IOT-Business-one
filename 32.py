import pandas as pd  

class SoftwareCostEstimator:  
    def __init__(self, blockchain_dev_cost_per_device, integration_platform_cost_per_device):  
        """  
        :param blockchain_dev_cost_per_device: هزینه توسعه بلاک‌چین به ازای هر دستگاه IoMT ( مبلغی برای هر دستگاه)  
        :param integration_platform_cost_per_device: هزینه پلتفرم یکپارچه‌سازی به ازای هر دستگاه IoMT  
        """  
        self.blockchain_dev_cost_per_device = blockchain_dev_cost_per_device  
        self.integration_platform_cost_per_device = integration_platform_cost_per_device  

    def estimate_costs(self, file_path):  
        try:  
            df = pd.read_csv(file_path)  
            print(f"فایل '{file_path}' با موفقیت بارگذاری شد. تعداد ردیف‌ها: {len(df)}")  
        except Exception as e:  
            print(f"خطا در خواندن فایل: {e}")  
            return  

        # فرض بر این است که ستون 'device_id' نماینده تعداد دستگاه‌های متفاوت IoMT است  
        if 'device_id' in df.columns:  
            num_devices = df['device_id'].nunique()  
            print(f"تعداد دستگاه‌های یکتا (IoMT) موجود در داده‌ها: {num_devices}")  
        else:  
            num_devices = 100  # مقدار پیش‌فرض در صورت نبود ستون  
            print(f"ستون 'device_id' یافت نشد. فرض بر تعداد دستگاه‌ها: {num_devices}")  

        # محاسبه هزینه‌ها  
        blockchain_dev_cost = num_devices * self.blockchain_dev_cost_per_device  
        integration_platform_cost = num_devices * self.integration_platform_cost_per_device  

        total_software_cost = blockchain_dev_cost + integration_platform_cost  

        print("\n--- خلاصه هزینه‌های نرم‌افزاری ---")  
        print(f"هزینه توسعه بلاک‌چین (برای {num_devices} دستگاه): {blockchain_dev_cost} واحد")  
        print(f"هزینه پلتفرم‌های یکپارچه‌سازی (برای {num_devices} دستگاه): {integration_platform_cost} واحد")  
        print(f"کل هزینه نرم‌افزاری: {total_software_cost} واحد\n")  

        return {  
            'num_devices': num_devices,  
            'blockchain_dev_cost': blockchain_dev_cost,  
            'integration_platform_cost': integration_platform_cost,  
            'total_software_cost': total_software_cost  
        }  


if __name__ == "__main__":  
    file_path = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv"  

    blockchain_dev_cost_per_device = 1000  # هزینه توسعه بلاک‌چین برای هر دستگاه  
    integration_platform_cost_per_device = 500  # هزینه پلتفرم‌های یکپارچه‌سازی برای هر دستگاه  

    estimator = SoftwareCostEstimator(blockchain_dev_cost_per_device, integration_platform_cost_per_device)  
    cost_summary = estimator.estimate_costs(file_path)  
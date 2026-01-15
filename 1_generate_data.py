import pandas as pd
import numpy as np
import time

def create_tesla_data():
    print("⚡ Starting GigaFactory Data Stream...")
    start = time.time()
    
    # 1,000,000 cells = True Big Data
    num_cells = 1000000 
    
    # Simulate the critical 'Tabless' welding process variables
    data = {
        'Cell_ID': np.arange(num_cells),
        'Laser_Weld_Power_kW': np.random.normal(15, 2, num_cells),
        'Weld_Time_ms': np.random.normal(250, 15, num_cells),
        'Internal_Resistance_mOhm': np.random.normal(5.4, 0.4, num_cells),
        'Jelly_Roll_Alignment_Error_mm': np.random.normal(0.05, 0.02, num_cells)
    }
    
    df = pd.DataFrame(data)

    # DEFINE THE FAILURE (SCRAP): 
    # If laser power is too high AND alignment is off, the weld "burns through" (Scrap)
    df['Is_Scrap'] = 0
    scrap_logic = (df['Laser_Weld_Power_kW'] > 18.5) & (df['Jelly_Roll_Alignment_Error_mm'] > 0.08)
    df.loc[scrap_logic, 'Is_Scrap'] = 1
    
    # Save the massive file
    df.to_csv('tesla_production_big_data.csv', index=False)
    print(f"✅ Success! Generated 1 Million records in {round(time.time()-start, 2)}s")

if __name__ == "__main__":
    create_tesla_data()
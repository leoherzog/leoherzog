#!/usr/bin/env python3
import requests
import time

# Use APKCombo API endpoint
apk_id = "com.happyfox.helpdesk"
download_url = f"https://apkcombo.com/happyfox-help-desk/{apk_id}/download/apk"

print(f"Attempting to download APK for {apk_id}")
print(f"URL: {download_url}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

try:
    # Try to get the download page
    response = requests.get(download_url, headers=headers, allow_redirects=True, timeout=30)
    
    # Check if we got an APK or HTML
    if 'application/vnd.android.package-archive' in response.headers.get('content-type', ''):
        with open('happyfox.apk', 'wb') as f:
            f.write(response.content)
        print(f"APK downloaded successfully: {len(response.content)} bytes")
    else:
        print("Response was not an APK file")
        print(f"Content-Type: {response.headers.get('content-type')}")
        
        # Try alternative: APKPure direct download
        print("\nTrying APKPure...")
        apkpure_url = "https://d.apkpure.com/b/APK/com.happyfox.helpdesk?version=latest"
        response = requests.get(apkpure_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            with open('happyfox.apk', 'wb') as f:
                f.write(response.content)
            print(f"APK downloaded from APKPure: {len(response.content)} bytes")
        else:
            print(f"Failed to download from APKPure: {response.status_code}")
            
except Exception as e:
    print(f"Error downloading APK: {e}")
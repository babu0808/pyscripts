import speedtest

def test_speed():
    st = speedtest.Speedtest()
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print(f"Download Speed: {download_speed:.2f} Mbps")

    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

    print("Fetching best server...")
    best_server = st.get_best_server()
    print(f"Connected to: {best_server['host']} in {best_server['country']} ({best_server['latency']:.2f} ms)")

if __name__ == "__main__":
    test_speed()

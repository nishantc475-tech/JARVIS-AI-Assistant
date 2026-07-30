import speedtest


def check_speed():

    try:

        st = speedtest.Speedtest()

        st.get_best_server()

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        return (
            f"Download Speed: {download:.2f} Mbps\n"
            f"Upload Speed: {upload:.2f} Mbps\n"
            f"Ping: {ping:.0f} ms"
        )

    except Exception as e:
        return str(e)
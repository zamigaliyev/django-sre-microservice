from prometheus_client import start_http_server, Counter

# Fərqli bir portda Prometheus HTTP serverini işə salın
start_http_server(8000)

# Metriklərinizi buradan qeyd edə bilərsiniz
c = Counter('my_failures', 'Description of counter')
c.inc()  # Sayacı artırın

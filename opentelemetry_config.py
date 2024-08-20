from opentelemetry.sdk.metrics.export import PrometheusMetricsExporter

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics.export import PrometheusMetricsExporter
from opentelemetry.instrumentation.django import DjangoInstrumentor

# Tracer provider və Resurs yaradılması
resource = Resource(attributes={
    "service.name": "django-microservice",
    "service.version": "1.0.0"
})

trace.set_tracer_provider(TracerProvider(resource=resource))

# Span Processor əlavə edin
tracer_provider = trace.get_tracer_provider()
exporter = PrometheusMetricsExporter(port=8000)  # Prometheus üçün bir export portu ayırın
tracer_provider.add_span_processor(BatchSpanProcessor(exporter))

# Django Instrumentor-u işə salın
DjangoInstrumentor().instrument()

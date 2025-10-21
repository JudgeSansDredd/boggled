{{- define "system.service.component" }}
---
apiVersion: v1
kind: Service
metadata:
  name: {{ .component.name }}-service
  labels:
{{ include "helper.metaLabels" . | indent 4 }}
spec:
  type: {{ .component.service.type }}
  selector:
    app: {{ .component.name }}
  ports:
{{- range .component.service.ports }}
  - protocol: {{ .protocol }}
    port: {{ .port }}
    targetPort: {{ .targetPort }}
    name: {{ .name }}
{{- end }}

{{- end }}
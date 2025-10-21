{{- define "system.persistent_volume.component" }}
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name:  "{{ .release.Name }}-{{ .component.name }}-pv"
  labels:
{{ include "helper.metaLabels" . | indent 4 }}
spec:
  storageClassName: {{ .volume.storageClassName }}
  persistentVolumeReclaimPolicy: {{ .volume.reclaimPolicy }}
  capacity:
    storage: {{ .volume.capacity.storage }}
  accessModes:
    {{ toYaml .volume.accessModes }}
{{- if .volume.hostPath }}
  hostPath:
    path: {{ .volume.hostPath }}
{{- end }}
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: "{{ .release.Name }}-{{ .component.name }}-pvc"
  labels:
{{ include "helper.metaLabels" . | indent 4 }}
spec:
  storageClassName: {{ .volume.storageClassName }}
  volumeName: "{{ .release.Name }}-{{ .component.name }}-pv"
  accessModes:
    {{ toYaml .volume.accessModes }}
  resources:
    requests:
      storage: {{ .volume.capacity.storage }}
{{- end }}

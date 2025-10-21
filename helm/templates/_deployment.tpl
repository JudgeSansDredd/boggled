{{- define "system.deployment.component" }}
{{ $image := .component.image }}
{{ $component := .component }}
{{ $release := .release }}
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ .component.name }}
  labels:
{{ include "helper.metaLabels" . | indent 4 }}
spec:
  replicas: 1
  selector:
    matchLabels:
{{ include "helper.matchLabels" . | indent 8 }}
  template:
    metadata:
      labels:
{{ include "helper.metaLabels" . | indent 8 }}
    spec:
{{- include "helper.affinity" . | indent 6 }}
{{- if $image.imagePullSecrets }}
      imagePullSecrets:
        - name: {{ toString $image.imagePullSecrets }}
{{- end }}
{{- if .component.volumes }}
{{- range $key, $volume := .component.volumes }}
      volumes:
        {{- if eq $volume.type "configMap" }}
        - name: "{{ $volume.name }}"
          configMap:
            name: "{{ $volume.name}}"
        {{- else }}
        - name: "{{ $release.Name }}-{{ $component.name }}-pvc"
          persistentVolumeClaim:
            claimName: "{{ $release.Name }}-{{ $component.name }}-pvc"
        {{- end }}
{{- end }}
{{- end }}
      containers:
        - name: {{ .component.name }}
{{ include "helper.deploy_tag" (dict "component" .component "values" .values "release" .release) | indent 10 }}
{{- if .component.deployment }}
  {{- toYaml .component.deployment | trim | nindent 10 }}
{{- end }}
{{- if .component.volumes }}
{{- range $key, $volume := .component.volumes }}
          volumeMounts:
          {{- if eq $volume.type "configMap" }}
            - name: {{ $volume.name }}
              mountPath: {{ $volume.mountPath }}
              subPath: {{ $volume.subPath }}
          {{- else }}
            - mountPath: {{ $volume.containerMountPath }}
              name: "{{ $release.Name }}-{{ $component.name }}-pvc"
          {{- end }}
{{- end }}
{{- end }}
{{- end }}

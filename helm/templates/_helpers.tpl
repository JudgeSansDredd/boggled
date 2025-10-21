{{/*
match labels
*/}}
{{- define "helper.matchLabels" -}}
app: {{ .component.name }}
{{- end }}

{{/*
meta labels
*/}}
{{- define "helper.metaLabels" -}}
app: {{ .component.name }}
tenant: {{ .values.system }}
{{- end }}

{{/*
Node Affinity helper
*/}}
{{- define "helper.affinity" -}}
{{- if .component.affinity -}}
nodeName: {{ .component.affinity }}
{{- end -}}
{{- end -}}

{{/*
Image name and tag helper
*/}}
{{- define "helper.image" -}}
image: "{{ .component.image.repository }}:{{ .component.image.tag }}"
{{- end -}}

{{- /* # returns one of the following
#  - image: current_release:current_tag from lookup
#  - image: current_release:deploy_tag from image lookup

# if this iteration of the loop has a .Values.deploy override tag
#   - set $new_image to the override tag
# else
#   - set $new_image to the current tag
*/ -}}
{{- define "helper.deploy_tag" -}}

  {{- $new_deployment := "" -}}
  {{- $component := .component.name -}}

  {{- $deployment := (lookup "apps/v1" "Deployment" .release.Namespace $component) | default dict }}
  {{- if $deployment -}}
    {{- $targetContainerName := $component -}}
    {{- $targetContainer := dict -}}
    {{- range $deployment.spec.template.spec.containers }}
      {{- if eq .name $targetContainerName }}
        {{- $targetContainer = . -}}
      {{- end -}}
    {{- end -}}

    {{- range $key, $deploy := .values.deploy -}}
      {{- if eq $key $component -}}
        {{- $new_deployment = $deploy.tag -}}
      {{- end -}}
    {{- end -}}

    {{- if $new_deployment -}}
image: "{{ .component.image.repository }}:{{ $new_deployment }}"
    {{- else -}}
image: {{ $targetContainer.image }}
    {{- end -}}
  {{- else -}}
image: "{{ .component.image.repository }}:{{ .component.image.tag }}"
  {{- end -}}
{{- end -}}


{{- /* include "helper.var_dump" . */ -}}
{{- define "helper.var_dump" -}}
{{- . | mustToPrettyJson | printf "\n%s" | fail }}
{{- end -}}

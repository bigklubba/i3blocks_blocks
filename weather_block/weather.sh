#!/bin/bash
# Based on http://openweathermap.org/current

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
API_KEY="52c8551a9d71dde5a242a125e4b70235"

# Check on http://openweathermap.org/find
ID_FROM_IP=$("${DIR}/get_city_id_from_ip.py")
if [ $? -eq 0 ]; then
  CITY_ID=$ID_FROM_IP
else
  CITY_ID="2663536"
fi
URGENT_LOWER=0
URGENT_HIGHER=30

ICON_SUNNY=""
ICON_CLOUDY=""
ICON_RAINY=""
ICON_STORM=""
ICON_SNOW=""
ICON_FOG=""

SYMBOL_CELSIUS="℃"

WEATHER_URL="http://api.openweathermap.org/data/2.5/weather?id=${CITY_ID}&appid=${API_KEY}&units=metric"

WEATHER_INFO=$(wget -qO- "${WEATHER_URL}")
WEATHER_MAIN=$(echo "${WEATHER_INFO}" | grep -o -e '\"main\":\"[a-Z]*\"' | awk -F ':' '{print $2}' | tr -d '"')
WEATHER_TEMP=$(echo "${WEATHER_INFO}" | grep -o -e '\"temp\":\-\?[0-9]*' | awk -F ':' '{print $2}' | tr -d '"')

if [[ "${WEATHER_MAIN}" = *Snow* ]]; then
  echo "${ICON_SNOW} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${ICON_SNOW} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
elif [[ "${WEATHER_MAIN}" = *Rain* ]] || [[ "${WEATHER_MAIN}" = *Drizzle* ]]; then
  echo "${ICON_RAINY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${ICON_RAINY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
elif [[ "${WEATHER_MAIN}" = *Cloud* ]]; then
  echo "${ICON_CLOUDY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${ICON_CLOUDY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
elif [[ "${WEATHER_MAIN}" = *Clear* ]]; then
  echo "${ICON_SUNNY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${ICON_SUNNY} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
elif [[ "${WEATHER_MAIN}" = *Fog* ]] || [[ "${WEATHER_MAIN}" = *Mist* ]]; then
  echo "${ICON_FOG} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${ICON_FOG} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
else
  echo "${WEATHER_MAIN} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo "${WEATHER_MAIN} ${WEATHER_TEMP}${SYMBOL_CELSIUS}"
  echo ""
fi

if [[ "${WEATHER_TEMP}" -lt "${URGENT_LOWER}" ]] || [[ "${WEATHER_TEMP}" -gt "${URGENT_HIGHER}" ]]; then
  exit 33
fi

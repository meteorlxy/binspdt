FROM python:3.6

ENV BINSPDT_APP_ROOT=/docker/binspdt
ENV BINSPDT_CONFIG_ROOT=${BINSPDT_APP_ROOT}/docker/config

COPY . ${BINSPDT_APP_ROOT}
WORKDIR ${BINSPDT_APP_ROOT}

RUN \
  APT_INSTALL="apt-get install -y --no-install-recommends" \
  PIP_INSTALL="pip3 install --no-cache-dir -i https://mirrors.xjtu.edu.cn/pypi/simple" \
  BUILD_PACKAGES="gettext-base" \
  set -x \
    # Install packages
    && sed -i -e "s/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g" -e "s/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list \
    && apt-get update \
    && ${APT_INSTALL} \
      nginx \
      supervisor \
      ${BUILD_PACKAGES} \
    && ${PIP_INSTALL} uwsgi \
    # Use envsubst to setup nginx config
    && envsubst '${BINSPDT_APP_ROOT} ${BINSPDT_CONFIG_ROOT}' < ${BINSPDT_CONFIG_ROOT}/nginx.template.conf > ${BINSPDT_CONFIG_ROOT}/nginx.conf \
    # Install python dependencies of binspdt
    && ${PIP_INSTALL} -r ${BINSPDT_APP_ROOT}/requirements.txt \
    # Extra setup
    && mkdir -p ${BINSPDT_APP_ROOT}/logs \
    && chown www-data:www-data -R ${BINSPDT_APP_ROOT} \
    # Clean up
    && apt-get purge -y gettext-base \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*

CMD ["/bin/sh", "-c", "supervisord -c ${BINSPDT_CONFIG_ROOT}/supervisord.conf"]

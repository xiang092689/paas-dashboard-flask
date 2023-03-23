FROM paasdashboard/paas-dashboard:flask-dep

COPY . /opt/paas-dashboard

WORKDIR /opt/paas-dashboard

RUN wget -q https://github.com/paas-dashboard/paas-dashboard-portal-angular/releases/download/latest/paas-dashboard-portal.tar.gz && \
    tar -xzf paas-dashboard-portal.tar.gz && \
    rm -rf paas-dashboard-portal.tar.gz

CMD ["/usr/bin/dumb-init", "bash", "-vx","/opt/paas-dashboard/scripts/start.sh"]

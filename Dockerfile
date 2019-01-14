FROM jmc1283/flasq-base

COPY . /home/flasq/site


#############################
#      Leave in here        #
# Annoying permission thing #
#      TODO: fix this       #
#############################
RUN chown -R flasq .        #
USER flasq                  #
#############################

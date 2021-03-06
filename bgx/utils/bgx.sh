#! /bin/sh
#
# bgx script


# PATH should only include /usr/* if it runs after the mountnfs.sh script
PATH=/sbin:/usr/sbin:/bin:/usr/bin:/usr/local/bin/
DESC="bgx"
NAME=bgx
LOGPATH="/var/log"
OUTFILE=$LOGPATH/bgx.log
PIDFILE=/var/run/$NAME.pid
VERBOSE=yes
DAEMON_ARGS="-d"
FROM="/home/bgx/Projects/bgx"
FROM1=""
DAEMON="docker-compose"
#
# Function that starts the daemon/service
#
do_start()
{
  (cd $FROM1;ls -l;docker-compose -f bgx/docker/docker-compose-netall-reg-dev-loc.yaml up $DAEMON_ARGS)
}

#
# Function that stops the daemon/service
#
do_stop()
{
        # Return
        #   0 if daemon has been stopped
        #   1 if daemon was already stopped
        #   2 if daemon could not be stopped
        #   other if a failure occurred
        (cd $FROM1;ls -l;docker-compose -f bgx/docker/docker-compose-netall-reg-dev-loc.yaml down)
}

case "$1" in
  start)
	[ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC " "$NAME"
	do_start
	case "$?" in
                0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
	esac
  ;;
  stop)
        [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
        do_stop
        case "$?" in
                0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
        esac
        ;;
  status)
       status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
       ;;
  restart|force-reload)
        [ "$VERBOSE" != no ] && log_daemon_msg "Restarting $DESC" "$NAME"
        do_stop
        do_start
        ;;
  *)
	echo "Usage: $SCRIPTNAME {start|stop|status|restart|force-reload}" >&2
	exit 1
	;;
esac

exit 0

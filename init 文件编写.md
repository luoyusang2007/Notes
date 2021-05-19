
```shell
#! /bin/bash                                                         
### BEGIN INIT INFO
#Provides:       touchfile
#Required-Start: $all
#Required-Stop:  $all
#Default-Start:  2 3 4 5
#Default-Stop:   0 1 6
#Short-Description:  Run Touchfile
#Description:    Run Touchfile
### END INIT INFO
TOUCHFILE="/var/tmp/touch.file"
case "$1" in
 start)
         echo "Creating $TOUCHFILE"
        touch $TOUCHFILE
 ;;
 stop)
         echo "Removing $TOUCHFILE"
        touch $TOUCHFILE
 ;;
 restart)
         echo "Recreating $TOUCHFILE"
        rm $TOUCHFILE
        touch $TOUCHFILE
 ;;
 reload)
         echo "Re-Touching $TOUCHFILE"
        touch $TOUCHFILE
 ;;
 *)
         echo "Usage: touchfile.sh <start|stop|restart|reload>"
 ;;
 esac
 exit 0


```



daemon-reload

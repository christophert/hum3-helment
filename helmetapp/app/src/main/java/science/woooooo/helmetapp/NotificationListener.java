package science.woooooo.helmetapp;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class NotificationListener extends Service {
    public NotificationListener() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
}

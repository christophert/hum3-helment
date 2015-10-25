package science.woooooo.helmetapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onRight(View view) {
        final TextView text = (TextView) findViewById(R.id.collision);
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "http://10.254.254.254/go/right";

        StringRequest strReq = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Log.d("ONRIGHT", response);
                text.setText(response);
                text.setVisibility(View.VISIBLE);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                text.setText("Error");
                text.setVisibility(View.VISIBLE);
            }
        });

        queue.add(strReq);
    }

    public void onLeft(View view) {
        final TextView text = (TextView) findViewById(R.id.collision);
        RequestQueue queue = Volley.newRequestQueue(this);
        String url = "http://10.254.254.254/go/left";

        StringRequest strReq = new StringRequest(Request.Method.GET, url, new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                Log.d("ONLEFT", response);
                text.setText(response);
                text.setVisibility(View.VISIBLE);
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                text.setText("Error");
                text.setVisibility(View.VISIBLE);
            }
        });

        queue.add(strReq);
    }
}

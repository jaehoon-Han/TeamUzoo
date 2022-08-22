package com.han.teamuzoo;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;

public class myplanetActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_myplanet);

//        Toolbar toolbar = (Toolbar) findViewById(R.id.chtl_toolbar);
//        setSupportActionBar(toolbar);

//        class Problems extends AppCompatActivity {
//            @Override
//            protected void onCreate(Bundle savedInstanceState) {
//                super.onCreate(savedInstanceState);
//                setContentView(R.layout.activity_myplanet);
//                LayoutInflater inflator = (LayoutInflater) this .getSystemService(Context.LAYOUT_INFLATER_SERVICE);
//                View v = inflator.inflate(R.layout.toolbar_myplanet, null);
//                getSupportActionBar().setCustomView(v);
//            }
//        }
    }
}
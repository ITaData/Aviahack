package com.example.sherbus

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        var a: int = 3
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
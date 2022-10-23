package com.example.sherbus

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import com.example.sherbus.ui.login.LoginFragment

class MainActivity : AppCompatActivity() {
    var login: String = ""
    var password: String = ""
    fun SaveDataUser(view: View){
        var login: EditText = findViewById(R.id.username)
        var password: EditText = findViewById(R.id.password)
        this.login = login.text.toString()
        this.password = password.text.toString()
        //Проверка по базе
        if(this.login == "Admin" && this.password == "1234"){
            setContentView(R.layout.activity_main)
        } else {
            Toast.makeText(this, "Ошибка. Проверьте введеные значения", Toast.LENGTH_SHORT).show()
        }
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.fragment_login)


    }
}
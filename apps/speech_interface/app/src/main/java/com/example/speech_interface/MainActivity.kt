package com.example.speech_interface

import android.graphics.BitmapFactory
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.github.bassaer.chatmessageview.model.ChatUser
import com.github.kittinunf.fuel.core.FuelManager
import java.util.*

class MainActivity : AppCompatActivity() {
    companion object {
        private const val ACCESS_TOKEN = "1234567890abcdef" // change to real API
    }
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // serves as authorization header
        FuelManager.instance.baseHeaders = mapOf(
            "Authorization" to "Bearer $ACCESS_TOKEN"
        )
        FuelManager.instance.basePath = "https://api.dialogflow.com/v1/"
        // set base parameter properties
        FuelManager.instance.baseParams = listOf(
            "v" to "20170712",                  // latest protocol
            "sessionId" to UUID.randomUUID(),   // random ID
            "lang" to "en"                      // English language
        )
        // configuring chat interface
        val human = ChatUser(
            1,
            "You",
            BitmapFactory.decodeResource(resources,
                R.drawable.ic_account_circle)
        )

        val agent = ChatUser(
            2,
            "Agent",
            BitmapFactory.decodeResource(resources,
                R.drawable.ic_account_circle)
        )

    }
}
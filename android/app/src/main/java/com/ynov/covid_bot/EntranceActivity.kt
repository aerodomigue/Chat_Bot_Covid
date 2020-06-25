package com.ynov.covid_bot

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import kotlinx.android.synthetic.main.activity_entrance.*
import org.jetbrains.anko.startActivity

class EntranceActivity : AppCompatActivity(), View.OnClickListener {


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_entrance)
        button.setOnClickListener(this)
    }


    override fun onClick(p0: View?) {
            when(p0?.id){
                R.id.button -> enterChatroom()
            }
    }

    private fun enterChatroom(){
        val userName = userName.text.toString()
        val roomName = roomname.text.toString()

        if(!roomName.isNullOrBlank()&&!userName.isNullOrBlank()) {
            val intentChatRoom = Intent(this, ChatRoomActivity::class.java)
            intentChatRoom.putExtra("userName", userName)
            intentChatRoom.putExtra("roomName", roomName)
            startActivity(intentChatRoom)

        }else{
            Toast.makeText(this,"Nickname and Roomname should be filled!",Toast.LENGTH_SHORT)
        }
    }
}

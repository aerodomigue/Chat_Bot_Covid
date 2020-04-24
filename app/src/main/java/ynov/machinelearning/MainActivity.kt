package ynov.machinelearning

import android.os.Bundle
import android.view.View
import android.widget.EditText
import androidx.appcompat.app.AppCompatActivity


class MainActivity : AppCompatActivity() {
    private var editText: EditText? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        try {
            this.supportActionBar!!.hide()
        } catch (e: NullPointerException) { }
        setContentView(R.layout.activity_main)
        // This is where we write the mesage
        editText = findViewById<View>(R.id.editText) as EditText
    }

    fun sendMessage(view: View?) {
        val message = editText!!.text.toString()
        if (message.length > 0) {
            editText!!.text.clear()

        }
    }
}
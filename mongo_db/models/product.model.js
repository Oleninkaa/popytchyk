
const mongoose = require('mongoose');

const UserSchema = mongoose.Schema(
    {

        name:{
            type: String,
            required: [true, "User name is required"],
        },

        surname:{
            type: String,
            required: [true, "User surname is required"],
        },

        phone:{
            type: String,
            required: [true, "User phone is required"],
        },

        email:{
            type: String,
            required: [true, "User email is required"],
        },

        start:{
            type: String,
            required: [true, "User start is required"],
        },

        finish:{
            type: String,
            required: [true, "User finish is required"],
        },

        date:{
            type: Date,
            required: [true, "User date is required"],
        },


        comment:{
            type: String,
            required: [false],
            default: 0,
        },

        
    },

    {
        timestamps:true
    }


);


const User = mongoose.model("User", UserSchema)

module.exports = User;
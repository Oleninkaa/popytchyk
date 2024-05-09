const express = require('express')
// Using Node.js `require()`
const mongoose = require('mongoose');
const app = express()
const User = require('./models/product.model.js');



const path = require('path');

//middleware
app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({extended:false}));

//routes
//app.use("/api/users", productRoute)

app.get('/', (req, res) => {

    res.sendFile(path.join(__dirname, 'public/start.html'));
    
});

app.get('/user', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/user.html'));
});

app.get('/admin', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/admin.html'));
});





app.get('/api/users', async(req, res) => {
    try {
        const products = await User.find({});
        res.status(200).json(products)
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});


app.get('/api/users/:id', async(req, res) => {
    try {
        const { id } = req.params; 
        const product = await User.findById(id)
        res.status(200).json(product)
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});


app.post('/api/users', async(req, res) => {
    try {
        const product = await User.create(req.body);
        res.status(200).json(product)
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});

//UPDATE

app.put('/api/users', async(req, res) => {
    try {
        const { _id, name, surname, phone, email, start, finish, date, comment } = req.body;
        
        const updatedUser = await User.findByIdAndUpdate(_id, {
            name: name,
            surname: surname,
            phone: phone,
            email: email,
            start: start,
            finish: finish,
            date: date,
            comment: comment
        }, { new: true });

        if (!updatedUser) {
            return res.status(404).json({ message: "User not found" });
        }

        res.status(200).json(updatedUser);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});


app.put('/api/users/:id', async(req, res) => {
    try {
        const { id } = req.params;
        
        const product = await User.findByIdAndUpdate(id, req.body)

        if(!product){
            res.status(404).json({message:"Prosuct not found"})
        }

        const updatedProduct = await User.findById(id);
        res.status(200).json(updatedProduct)

    } catch (error) {
        res.status(500).json({message:error.message})
    }
});





//DELETE

app.delete('/api/users/:id', async(req, res) => {
    try {
        console.log(req.params)
        const { id } = req.params; 
        
        
        const deleteUser = await User.findByIdAndDelete(id)

        if(!deleteUser){
            res.status(404).json({message:"Product not found"})
        }

        
        res.status(200).json("Deleted successfully")
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

/*





app.post('/api/products', async(req, res) => {
    try {
        const product = await Product.create(req.body);
        res.status(200).json(product)
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});




//UPDATE

app.put('/api/product/:id', async(req, res) => {
    try {
        const { id } = req.params;
        const product = await Product.findByIdAndUpdate(id, req.body)

        if(!product){
            res.status(404).json({message:"Prosuct not found"})
        }

        const updatedProduct = await Product.findById(id);
        res.status(200).json(updatedProduct)

    } catch (error) {
        res.status(500).json({message:error.message})
    }
});




//DELETE

app.delete('/api/product/:id', async(req, res) => {
    try {
        const { id } = req.params;
        const product = await Product.findByIdAndDelete(id)

        if(!product){
            res.status(404).json({message:"Product not found"})
        }

        
        res.status(200).json("Deleted successfully")

    } catch (error) {
        res.status(500).json({message:error.message})
    }
});

*/

mongoose.connect("mongodb+srv://admin:admin@poputchyk.twcjme5.mongodb.net/Poputchyk?retryWrites=true&w=majority&appName=Poputchyk")
.then(()=>{
    console.log("Connected to database!")
    app.listen(3000, () => {
        console.log('Server is running on port 3000');
    });
})
.catch(()=>{
    console.log("Connection failed")
})
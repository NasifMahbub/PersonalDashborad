import React, { Component } from 'react';
import './layout/home.css';
import axios from 'axios';

class Home extends Component {

  constructor() {
    super();
    this.state = {
      id: null,
      username: null,
      first_name: null,
      last_name: null,
      email: null,
      contact_no: null,
      image: null
    };
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/users/api/v1/2/')
      .then(res => {
        const data = res.data;
        console.log(data);
        this.setState({id: data.id, username : data.username, 
          first_name : data.first_name, last_name : data.last_name,
          email: data.email, contact_no: data.contact_no, image: data.image
        })
      })
  }

  render() {
    return (
      <div className="Home">
        <header className="Home-header">
          <p>Personal Dashboard</p>
        </header>
        <div className="Home-body">
          <h1>Welcome</h1>
          <p>This is the personal dashboard of {this.state.username} </p>
          <p>Name: {this.state.first_name}  {this.state.last_name}</p>
          <p>Email: {this.state.email}</p>
          <p>Contact No: {this.state.contact_no}</p>
          
          <img src={this.state.image} alt="" />
          <p></p>
        </div>
      </div>
    )
  }
}

export default Home;
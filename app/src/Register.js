import React, { Component } from "react";
import {
  Redirect
} from "react-router-dom";
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';


class Register extends Component {
    constructor(props) {
        super(props);
        this.state = {
            email: "",
            username: "",
            password: "",
            password2: "",
            errorMessage: ""
        };
    }

    render() {
        return (
        <div
            style={{display: "flex", flexDirection: "column", alignItems: "start"}}
        >
            <h1>Registration</h1>
            <TextField
                label = "Email"
                value = {this.state.email}
                onChange = {e => this.setState({email: e.target.value})}
            />
            <TextField
                label = "Username"
                value = {this.state.username}
                onChange = {e => this.setState({username: e.target.value})}
            />
            <TextField
                label = "Password"
                type="password"
                value = {this.state.password}
                onChange = {e => this.setState({password: e.target.value})}
            />
            <TextField
                label = "Confirm Password"
                type="password"
                value = {this.state.password2}
                onChange = {e => this.setState({password2: e.target.value})}
            />
            <div
                style={{display: "flex", flexDirection: "row", alignItems: "start"}}
            >
                <Button variant = "contained"
                    onClick = {() => this.submit("Visitor")}
                >Register Visitor</Button>
                <Button variant = "contained"
                    onClick = {() => this.submit("Staff")}
                >Register Staff</Button>
            </div>
            <p>{this.state.errorMessage}</p>
        </div>
        );
    }

    submit(userType) {
        if(this.state.password !== this.state.password2) {
            this.setState({errorMessage: "Passwords do not match"});
        } else {
            this.register(this.state.email, this.state.username, this.state.password, userType).then((result) => {
                if(result.registerSuceeded) {
                    this.props.onRegister(result.username, result.userType, result.authToken);
                } else {
                    this.setState({errorMessage: result.errorMessage});
                }
            });
        }
    }

    register(email, username, password, userType) {
        if(username === "bob") {
            return Promise.resolve({
                registerSuceeded: true,
                authToken: "auth",
                username: "user",
                userType: "Visitor"
            });
        } else {
            return Promise.resolve({
                registerSuceeded: false,
                errorMessage: "Error"
            });
        }
    }
}

export default Register;

import React, { Component } from "react";
import {
  Redirect
} from "react-router-dom";
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';


class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: "", errorMessage: ""};
    }

    render() {
        return (
        <div
            style={{display: "flex", flexDirection: "column", alignItems: "start"}}
        >
            <h1>Login</h1>
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
            <Button variant = "contained"
                onClick = {this.submit.bind(this)}
            >Login</Button>
            <p>{this.state.errorMessage}</p>
        </div>
        );
    }

    submit() {
        this.login(this.state.username, this.state.password).then((result) => {
            if(result.loginSuceeded) {
                this.props.onLogin(result.username, result.userType, result.authToken)
            } else {
                this.setState({errorMessage: result.errorMessage})
            }
        });

    }

    login(username, password) {
        if(username == password) {
            return Promise.resolve({
                loginSuceeded: true,
                authToken: "auth",
                username: "user",
                userType: "Visitor"
            });
        } else {
            return Promise.resolve({
                loginSuceeded: false,
                errorMessage: "Error"
            });
        }
    }
}

export default Login;

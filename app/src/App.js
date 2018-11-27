import React, { Component } from "react";

import Home from "./Home";
import Test from "./Test";
import Login from "./Login"
import Register from "./Register"
import SearchExhibits from "./SearchExhibits"

import "./App.css"

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {page: <Home />, userType: null, username: null, authToken: null};
    }

    render() {
        switch(this.state.userType) {
            case "Admin":
                var header = null;
                break;
            case "Staff":
                var header = null;
                break;
            case "Visitor":
                var header = (
                    <div className = {"header"}>
                        <HeaderLink
                            text = {"Search Exhibits"}
                            page = {<SearchExhibits />}
                            navigate = {this.navigate.bind(this)}
                        />
                        <p
                            onClick = {() => this.logout()}
                            className = "headerLink"
                        >
                            Logout
                        </p>
                    </div>
                );
                break;
            default:
                var header = (
                    <div className = {"header"}>
                        <HeaderLink
                            text = {"Home"}
                            page = {<Home />}
                            navigate = {this.navigate.bind(this)}
                        />
                        <HeaderLink
                            text = {"Login"}
                            page = {<Login onLogin = {this.login.bind(this)} />}
                            navigate = {this.navigate.bind(this)}
                        />
                        <HeaderLink
                            text = {"Register"}
                            page = {<Register onRegister = {this.login.bind(this)} />}
                            navigate = {this.navigate.bind(this)}
                        />
                    </div>
                )
        }
        return (
            <div>
                <h1>Test App</h1>
                {header}
                {this.state.page}
            </div>
        );
    }

    navigate(page) {
        this.setState({page: page})
    }

    login(username, userType, authToken) {
        this.setState({username: username, userType: userType, authToken: authToken, page: <Home />})
    }

    logout() {
        this.setState({
            username: "",
            userType: "",
            authToken: "",
            page: <Home />
        })
    }
}

class HeaderLink extends Component {
    render() {
        return (
            <p
                onClick = {() => this.props.navigate(this.props.page)}
                className = "headerLink"
            >
                {this.props.text}
            </p>
        )
    }
}

export default App;

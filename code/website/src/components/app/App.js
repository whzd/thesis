import React, { Component } from 'react';
import 'antd/dist/antd.css';
import './App.css';
import Navbar from '../navbar/Navbar.js';
import Search from '../search/Search.js';
import Display from '../display/Display.js';
import Avatar from '../avatar/Avatar.js';
import { Layout, Row, Col } from 'antd';
import explanation from '../../apis/Explanation.js';

const { Header, Footer, Content } = Layout;

class App extends Component {

    state = {
        explanations: null,
        showAvatar: false
    }

    handleSubmit = async (conceptFromSearch) => {
        const response = await explanation.get('/search', {
            params: {
                query: conceptFromSearch
            }
        })
        console.log(response.data)
        this.setState({
            explanations: response.data,
        })
    };

    handleAvatar = (value) => {
        this.setState({
           showAvatar: value
        })
    }

    render() {
        return (
            <div className="App">
                <Layout className="layout">
                    <Header>
                        <Row justify="center">
                            <Col xs={ 6 } sm={ 5 } md={ 4 } lg={ 3 } xl={ 2 }><div className="logo" /></Col>
                            <Col xs={ 18 } sm={ 14 } md={ 15 } lg={ 16 } xl={ 18 }><h1> <b>E</b>xplicação <b>A</b>utomática de <b>C</b>onceitos </h1></Col>
                            <Col xs={ 0 } sm={ 5 } md={ 4 } lg={ 3 } xl={ 2 }><Navbar /></Col>
                        </Row>
                    </Header>
                    <Content style={{ padding: '0 50px' }}>
                        <div className="site-layout-content">
                            <Row justify="center">
                                <Col xs={ 24 } sm={ 24 } md={ 24 } lg={ 24 } xl={ 24 }><Search handleFormSubmit={this.handleSubmit}/></Col>
                            </Row>
                            <br />
                            <br />
                            <Row justify="center">
                                <Col xs={ 24 } sm={ 12 } md={ 12 } lg={ 14 } xl={ 14 }><Display content={this.state.explanations} handleAvatar={this.handleAvatar}/></Col>
                                <Col xs={ 0 } sm={ 12 } md={ 8 } lg={ 4 } xl={ 6 }><Avatar show={this.state.showAvatar}/></Col>
                            </Row>
                        </div>
                    </Content>
                    <Footer style={{ textAlign: 'center' }}>GILT ©2016</Footer>
                </Layout>
            </div>
        )
    }
}

export default App;

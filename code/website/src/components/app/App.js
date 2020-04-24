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
        explanations: [],
        flag: false
    }

    handleSubmit = async (conceptFromSearch) => {
        const response = await explanation.get('/search', {
            params: {
                query: conceptFromSearch
            }
        })
        console.log(response.data)
        this.setState({
            explanations: response.data.resp,
            flag: true
        })
    };

    render() {
        return (
            <div className="App">
            <h1> Welcome! </h1>
            <Layout className="layout">
            <Header>
            <div className="logo" />
            <Navbar />
            </Header>
            <Content style={{ padding: '0 50px' }}>
            <div className="site-layout-content">
            <Search handleFormSubmit={this.handleSubmit}/>
            <Row>
                <Col flex={4}><Display string={this.state.explanations}/></Col>
                <Col flex={1}><Avatar show={this.state.flag}/></Col>
            </Row>
            </div>
            </Content>
            <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
            </Layout>
            </div>
        )
    }
}

export default App;

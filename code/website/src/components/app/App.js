import React, { Component } from 'react';
import 'antd/dist/antd.css';
import './App.css';
import Navbar from '../navbar/Navbar.js';
import Search from '../search/Search.js';
import Explanation from '../explanation/Explanation.js';
import Avatar from '../avatar/Avatar.js';
import { Layout, Row, Col } from 'antd';

const { Header, Footer, Content } = Layout;

class App extends Component {
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
            <Search />
            <Row>
                <Col flex={4}><Explanation /></Col>
                <Col flex={1}><Avatar /></Col>
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

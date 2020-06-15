import React, { Component } from 'react';
import { Card, Collapse, Popconfirm, message, Alert } from 'antd';
import { CameraOutlined, DislikeOutlined, LikeOutlined } from '@ant-design/icons';
import './Display.css';

const { Panel } = Collapse;

function confirm(e) {
    console.log(e);
    message.success('Click no Sim');
}

function cancel(e) {
    console.log(e);
    message.error('Click on Não');
}


class Display extends Component {



    render() {
        let displayContent
        let moreInfo
        let definition
        let feedback
        if(this.props.content != null) {
            if (this.props.content.definition[0] == "Não foram encontrados resultados."){
                displayContent = <div><Alert
                    message="Erro!"
                    description="Não foram encontrados resultados."
                    type="error"
                    showIcon
                /></div>
            }else{
                feedback =
                    <div>
                            Feedback:
                        <a href="#"><LikeOutlined /></a>
                        <Popconfirm
                            title="Deseja uma nova explicação?"
                            onConfirm={confirm}
                            onCancel={cancel}
                            okText="Sim"
                            cancelText="Não"
                        >
                            <a href="#"><DislikeOutlined /></a>
                        </Popconfirm>
                    </div>

                    moreInfo = this.props.content.additionalInfo.map((item, index) => (
                        <p><a href={item} key={index}>{item}</a></p>
                    ));

                definition = this.props.content.definition.map((item, index) => (
                    <div id={index}>
                        <Card title={`${index+1}. ${this.props.content.expression}`} style={{ width: '90%' }}>
                            <p>{item[0]} <a href={`https://www.google.com/search?q=${item[0]}&tbm=isch`} target="_blank"><CameraOutlined /></a></p>
                            <br />
                                {feedback}
                        </Card>
                        <br />
                    </div>
                ));

                displayContent =
                    <div>
                            {definition}
                        <Collapse accordion style={{ width: '90%' }}>
                            <Panel header="Fontes" key="1">
                                <p><a href={this.props.content.source}>{this.props.content.source}</a></p>
                            </Panel>
                            <Panel header="Informação Adicional" key="2">
                                    {moreInfo}
                            </Panel>
                        </Collapse>
                    </div>
            }
        }else{
            displayContent = ""
        }

        return (
            <div className="Display">
                    { displayContent }
            </div>
        )
    }
}

export default Display;

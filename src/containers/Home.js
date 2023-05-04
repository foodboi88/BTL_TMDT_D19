import PropTypes from "prop-types";
import React, { Component } from "react";
import {
  Button,
  Container,
  Divider,
  Grid,
  Header,
  Image,
  Responsive,
  Segment,
  Sidebar,
  Visibility
} from "semantic-ui-react";
import Home1 from "../assets/home_1.jpg"
import Home2 from "../assets/home_2.jpg"
import Home3 from "../assets/home_3.webp"

const getWidth = () => {
  const isSSR = typeof window === "undefined";
  return isSSR ? Responsive.onlyTablet.minWidth : window.innerWidth;
};

class DesktopContainer extends Component {
  state = {};

  hideFixedMenu = () => this.setState({ fixed: false });
  showFixedMenu = () => this.setState({ fixed: true });

  render() {
    const { children } = this.props;

    return (
      <Responsive getWidth={getWidth} minWidth={Responsive.onlyTablet.minWidth}>
        <Visibility
          once={false}
          onBottomPassed={this.showFixedMenu}
          onBottomPassedReverse={this.hideFixedMenu}
        />
        {children}
      </Responsive>
    );
  }
}

DesktopContainer.propTypes = {
  children: PropTypes.node
};

class MobileContainer extends Component {
  state = {};

  handleSidebarHide = () => this.setState({ sidebarOpened: false });

  handleToggle = () => this.setState({ sidebarOpened: true });

  render() {
    const { children } = this.props;

    return (
      <Responsive
        as={Sidebar.Pushable}
        getWidth={getWidth}
        maxWidth={Responsive.onlyMobile.maxWidth}
      >
        {children}
      </Responsive>
    );
  }
}

MobileContainer.propTypes = {
  children: PropTypes.node
};

const ResponsiveContainer = ({ children }) => (
  <div>
    <DesktopContainer>{children}</DesktopContainer>
    <MobileContainer>{children}</MobileContainer>
  </div>
);

ResponsiveContainer.propTypes = {
  children: PropTypes.node
};

const HomepageLayout = () => (
  <ResponsiveContainer>
    <Segment style={{ padding: "2em 0em" }} vertical>
      <Grid container stackable verticalAlign="middle">
        <Grid.Row>
          <Grid.Column width={8}>
            <Header as="h3" style={{ fontSize: "2em" }}>
              Về chúng tôi
            </Header>
            <p style={{ fontSize: "1.33em" }}>
              Shopgiaydieucay.com
            </p>
            <Header as="h3" style={{ fontSize: "2em" }}>
              Uy tín lâu năm chuyên cung cấp giày thể thao sneaker nam, nữ hàng Replica 1:1 - Like Auth với chất lượng khác biệt so với thị trường và giá tốt nhất. 
            </Header>
            <p style={{ fontSize: "1.33em" }}>
            Bạn không đủ hầu bao để mua 1 đôi Chính Hãng? Hay bạn order quá lâu cũng như size của mình đã Sold Out? Bạn đang cần tìm các mẫu Sneaker với mong muốn chất lượng, detail chuẩn hàng Auth? Shopgiayreplica.com sẽ giải quyết hết thắc mắc của bạn với chất lượng cực kỳ khác biệt, đa dạng mẫu mã, có sẵn hàng. Liên tục cập nhật, update, fix các phiên bản tiệm cận hàng Auth nhất. Các bạn có thể yên tâm lựa chọn trong một thị trường rất hỗn loạn về chất lượng, cũng như định nghĩa chuẩn về Giày Replica - Like Auth.
            </p>
          </Grid.Column>
          <Grid.Column floated="right" width={6}>
            <Image
              bordered
              rounded
              size="large"
              src={Home1}
              style={{width: "140%"}}
            />
          </Grid.Column>
        </Grid.Row>
        <Grid.Row>
          <Grid.Column textAlign="center">
            <Button size="huge">Check hàng ngay nào</Button>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
    <Segment style={{ padding: "0em" }} vertical>
      <Grid celled="internally" columns="equal" stackable>
        <Grid.Row textAlign="center">
          <Grid.Column style={{ paddingBottom: "5em", paddingTop: "5em" }}>
            <Header as="h3" style={{ fontSize: "2em" }}>
              Air Force 1 Louis Vuitton hàng Best Quality
            </Header>
            <p style={{ fontSize: "1.33em" }}>
              <Image src={Home3} />

              Hàng đẹp nhất thị trường hiện tại, vân dập nét căng, chất da bò dày, đường chỉ may đều và gọn. Có sẵn tại shop 1 vài size, giá 5tr5. Bạn có thể trực tiếp đến xem hàng tại shop.
            </p>
          </Grid.Column>
          <Grid.Column style={{ paddingBottom: "5em", paddingTop: "5em" }}>
            <Header as="h3" style={{ fontSize: "2em" }}>
            Giày Air Jordan 1 Low Blue Siêu Cấp TT
            </Header>
            <p style={{ fontSize: "1.33em" }}>
              <Image src={Home2} />
              Phiên bản Air Jordan 1 Low mới nhất của Nike đã được bổ sung một phối màu cực hiếm, chắc chắn sẽ gây ra sự cạnh tranh giữa các tín đồ giày.
            </p>
          </Grid.Column>
        </Grid.Row>
      </Grid>
    </Segment>
    <Segment style={{ padding: "8em 0em" }} vertical>
      <Container text>
        <Header as="h3" style={{ fontSize: "2em" }}>
        Siêu phẩm Nike Air Jordan 1 x Dior có gì HOT?
        </Header>
        <p style={{ fontSize: "1.33em" }}>
        Trong suốt những năm phát triển, Nike đã liên tục cho ra đời những phiên bản hot và Nike Air Jordan 1 x Dior là một trong số những siêu phẩm như vậy. Giới mộ điệu đánh giá đây là mẫu hàng được mong đợi nhất trong năm 2020.
        </p>
        <Button as="a" size="large">
          Đọc ngay cho nóng nào
        </Button>
        <Divider
          as="h4"
          className="header"
          horizontal
          style={{ margin: "3em 0em", textTransform: "uppercase" }}
        >
          <a href="#case-studies">Tin tiếp</a>
        </Divider>
        <Header as="h3" style={{ fontSize: "2em" }}>
        Phối đồ cùng Nike Air Jordan 1 như thế nào để vừa sang vừa chất
        </Header>
        <p style={{ fontSize: "1.33em" }}>
        Air Jordan 1 (AJ1) chính là độ fit hoàn hảo với nhiều gu thời trang và phù hợp với mọi lứa tuổi. Tuy nhiên, bất kỳ món đồ nào khi phối với nhau đều có quy tắc và cách để khiến chúng vừa hài hoà, vừa chất chơi cũng không phải quá dễ dàng. Chính vì vậy, Shopgiaydieucay.com sẽ bất mí những cách phối đồ với giày Jordan 1 và một số mẹo giúp bạn trở nên thật nổi bật cùng “đôi giày huyền thoại” này ngay trong bài viết dưới đây.
        </p>
        <Button as="a" size="large">
        Đọc ngay cho nóng nào
        </Button>
      </Container>
    </Segment>
  </ResponsiveContainer>
);
export default HomepageLayout;

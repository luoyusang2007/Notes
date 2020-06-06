https://www.sohu.com/a/280388046_505923
https://www.jianshu.com/p/ff9d3ad817ca

# OpenID: Authentication 认证
“这个用户是本服务的用户，我已验证过他就是XXX”

## 步骤




# OAuth: Authorization 授权
“这个用户是本服务的用户，我已验证过他就是XXX，你可以使用本服务中他的XXX信息”。因为授权其实是认证+授权两步，所以也具有认证的功能。

## 步骤（2.0）
假设站点A要请求站点B用户的权限
- 用户在站点A页面点击 用站点B账户登录 

# SAML【已废弃】


## 步骤（2.0）
SP: Service Provider （如CSDN用腾讯登录，CSDN服务器）
IdP: ID Provider （腾讯认证服务器）
- 你访问SP网页，要用IdP账号登陆
- SP 向 IDP 发送了一个 SAML 认证请求，同时 SP 将 用户浏览器重定向到 IDP
- IDP 在验证完来自 SP 的 请求无误 之后，在浏览器中呈现 登陆表单 让用户填写 用户名 和 密码 进行登陆。
- 一旦用户登陆成功， IDP 会生成一个包含 用户信息（用户名 或者 密码）的 SAML token（SAML token 又称为 SAML Assertion，本质上是 XML 节点）。IDP 向 SP 返回 token，并且将 用户重定向 到 SP (token 的返回是在 重定向步骤 中实现的)。
- SP 对拿到的 token 进行验证，并从中解析出 用户信息，例如 用户是谁 以及 用户的权限 有哪些。此时就能够根据这些信息允许用户访问我们网站的内容。


# 单点登录SSO



# OpenStack Keystone 的认证
https://blog.csdn.net/hejin_some/article/details/58066427


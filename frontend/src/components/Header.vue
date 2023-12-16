<template>
  <header>
    <div class="header-fon">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <nav class="navbar navbar-expand-lg navbar-dark">
              <div class="container mt-3 menu">
                <a class="navbar-brand display-6 logo" href="#">GoTravel</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                  data-bs-target="#collapsibleNavbar">
                  <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse justify-content-end " id="collapsibleNavbar">
                  <ul class="navbar-nav">
                    <li class="nav-item menu">
                      <a id="personalplace" class="nav-link active px-4" href="/home">个人中心</a>
                    </li>
                  </ul>
                  <button id="LR" type="button" class="btn btn-danger px-4 py-2 button-1" onclick="LR()">登录 | 注册</button>
                </div>
              </div>
            </nav>
          </div>
        </div>
      </div>

      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12">
            <div class="main-flex">
              <div class="second-flex">
                <div class="title">
                  <h1 class="heading-1">随心而行<br> 步向未知的诗和远方</h1>
                  <p class="text-1">旅行，是心灵的独白，是梦想的延伸。在每一次的行走中，我们都是故事的主人，<br>用心感受那些美好瞬间，将它们串联成生命中最美的记忆。</p>
                  <button id="randomgo" type="button" class="btn btn-danger px-4 py-2 button-2"
                    onclick=" randomgo()">说走就走</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
